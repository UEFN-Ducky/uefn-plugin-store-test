"""Minimal Store test plugin — register only."""


def register(api) -> None:
    api.log("store-test plugin loaded")
