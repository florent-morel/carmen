"""
Tests for the Prometheus Query Builder.
"""

from backend.src.crud.prometheus_query_builder import PromQBuilder


def test_basic_metric_with_labels():
    """
    Test basic metric with labels.
    """
    query = (
        PromQBuilder().metric("http_requests_total", job="api", method="GET").build()
    )
    expected = 'http_requests_total{job=~"api", method=~"GET"}'
    assert query == expected


def test_sum_by():
    """
    Test sum by labels.
    """
    query = (
        PromQBuilder()
        .metric("http_requests_total", job="api")
        .sum_by("instance")
        .build()
    )
    expected = 'sum by (instance) (http_requests_total{job=~"api"})'
    assert query == expected


def test_group_by():
    """
    Test group by labels.
    """
    query = (
        PromQBuilder()
        .metric("container_memory_usage_bytes", container="nginx")
        .group_by("pod", "namespace")
        .build()
    )
    expected = (
        'group by (pod, namespace) (container_memory_usage_bytes{container=~"nginx"})'
    )
    assert query == expected


def test_binary_op_with_on_and_group_left():
    """
    Test binary operation with on and group_left modifiers.
    """
    left = (
        PromQBuilder()
        .metric("pod:container_cpu_usage:sum", namespace="prod")
        .sum_by("pod")
    )
    right = PromQBuilder().metric("kube_pod_labels", app="nginx")

    query = left.op(
        "*", right, on=["pod"], grouping_side="left", grouping_labels=["app"]
    ).build()

    expected = (
        'sum by (pod) (pod:container_cpu_usage:sum{namespace=~"prod"}) '
        "* on(pod) group_left(app) "
        '(kube_pod_labels{app=~"nginx"})'
    )
    assert query == expected


def test_complex_chaining():
    """
    Test complex chaining of methods.
    """
    query = (
        PromQBuilder()
        .metric("node_cpu_seconds_total", mode="idle", instance="node-1")
        .sum_by("instance")
        .build()
    )
    expected = (
        'sum by (instance) (node_cpu_seconds_total{mode=~"idle", instance=~"node-1"})'
    )
    assert query == expected
