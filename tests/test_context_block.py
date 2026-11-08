#!/usr/bin/env python3
"""Tests for context_block.py port of claude-mem helpers."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from context_block import find_context_block_range, strip_context_blocks, inject_context_block


def test_find_simple():
    text = "before\n<claude-mem-context>\ncontent\n</claude-mem-context>\nafter"
    result = find_context_block_range(text)
    assert result is not None
    start, end = result
    assert text[start:end] == "<claude-mem-context>\ncontent\n</claude-mem-context>"


def test_find_none():
    text = "no tags here"
    assert find_context_block_range(text) is None


def test_find_unclosed():
    text = "<claude-mem-context>\ncontent"
    assert find_context_block_range(text) is None


def test_find_multiple():
    text = "<tag-a>\nfirst\n</tag-a>\nmiddle\n<tag-b>\nsecond\n</tag-b>"
    result = find_context_block_range(text, tag='tag-a')
    assert result is not None
    start, end = result
    assert text[start:end] == "<tag-a>\nfirst\n</tag-a>"
    result_b = find_context_block_range(text, tag='tag-b')
    assert result_b is not None


def test_strip():
    text = "before\n<claude-mem-context>\ncontent\n</claude-mem-context>\nafter"
    result = strip_context_blocks(text)
    assert result == "before\n\nafter"


def test_strip_multiple():
    text = "a\n<claude-mem-context>\nx\n</claude-mem-context>\nb\n<claude-mem-context>\ny\n</claude-mem-context>\nc"
    result = strip_context_blocks(text)
    assert "<claude-mem-context>" not in result
    assert "a" in result and "b" in result and "c" in result


def test_inject_new():
    text = "Some text"
    result = inject_context_block(text, 'claude-mem-context', 'new content')
    assert "<claude-mem-context>" in result
    assert "new content" in result


def test_inject_replace():
    text = "before\n<claude-mem-context>\nold\n</claude-mem-context>\nafter"
    result = inject_context_block(text, 'claude-mem-context', 'new')
    assert "new" in result
    assert "old" not in result
    assert "before" in result
    assert "after" in result


def test_inject_with_header():
    text = "Some text"
    result = inject_context_block(text, 'claude-mem-context', 'content', header='## Header')
    assert "## Header" in result
    assert "<claude-mem-context>" in result


def test_fence_ignores_tag():
    text = "text\n```\n<claude-mem-context>\nnot a real tag\n```\nmore"
    result = find_context_block_range(text)
    assert result is None


if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"FAIL {t.__name__}: {e}")
            failed += 1
    print(f"{passed} passed, {failed} failed")
