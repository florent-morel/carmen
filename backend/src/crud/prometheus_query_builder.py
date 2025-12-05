"""
This module define the PromQBuilder class, which provides a fluent interface for building Prometheus queries (PromQL).
"""

from __future__ import annotations


class PromQBuilder:
    """
    A class to build Prometheus queries using a fluent interface.
    This class allows for the construction of complex PromQL queries through method chaining.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the PromQBuilder class with an empty query.
        """
        self._query: str = ""

    @property
    def query(self) -> str:
        """
        Returns the current query string.

        :return: The constructed query string.
        """
        return self._query

    def metric(self, metric_name: str, **labels: str) -> PromQBuilder:
        """
        Initializes the query with the given metric name and optional label matchers.

        :param metric_name: The name of the Prometheus metric.
        :param labels: Key-value pairs representing label matchers (regex supported).
        :return: self, for method chaining.
        """
        self._query = f"""{metric_name}{{{", ".join([f'{k}=~"{v}"' for k, v in labels.items()])}}}"""
        return self

    def sum_by(self, *labels: str) -> PromQBuilder:
        """
        Adds a `sum by(...)` aggregation to the current query.

        :param labels: Label names to group by in the sum.
        :return: self, for method chaining.
        """
        self._query = f"sum by ({', '.join(labels)}) ({self._query})"
        return self

    def group_by(self, *labels: str) -> PromQBuilder:
        """
        Adds a `group by(...)` wrapper to the current query.

        :param labels: Label names to group by.
        :return: self, for method chaining.
        """
        self._query = f"group by ({', '.join(labels)}) ({self._query})"
        return self

    def op(
        self,
        operator: str,
        other: PromQBuilder,
        on: list[str],
        grouping_side: str,
        grouping_labels: list[str],
    ) -> PromQBuilder:
        """
        Combines the current query with another using the specified operator and join modifiers.

        :param operator: Binary operator (e.g., "+", "-", "*", "/").
        :param other: Another PromQBuilder instance to combine with.
        :param on: List of labels to join on.
        :param grouping_side: Which side to apply grouping on ("left" or "right").
        :param grouping_labels: Labels to group on for the specified side.
        :return: self, for method chaining.
        """
        modifiers = []
        if on:
            modifiers.append(f"on({', '.join(on)})")
        if grouping_side:
            side_func = f"group_{grouping_side}"
            modifiers.append(f"{side_func}({', '.join(grouping_labels)})")
        modifier_str = " ".join(modifiers)
        self._query = f"{self._query} {operator} {modifier_str} ({other.query})"
        return self

    def build(self) -> str:
        """
        Returns the constructed PromQL query string.

        :return: Final Prometheus query as a string.
        """
        return self._query
