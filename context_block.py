#!/usr/bin/env python3
"""Port of claude-mem's findContextBlockRange and related helpers to Python.

Functions:
  find_context_block_range(text, tag) -> (start, end) or None
  strip_context_blocks(text, tag) -> text with <tag>...</tag> removed
  inject_context_block(text, tag, content, header=None) -> text with block replaced or appended
"""
import re

TAG_RE = re.compile(r'^( {0,3})(\S+)[ \t]*$')
FENCE_RE = re.compile(r'^ {0,3}(`{3,}|~{3,})(.*)$')


def find_context_block_range(text, tag='claude-mem-context'):
    """Return (start, end) indices of <tag>...</tag> block, or None.
    Ignores tags inside fenced code blocks."""
    open_tag = f'<{tag}>'
    close_tag = f'</{tag}>'
    open_len = len(open_tag)
    close_len = len(close_tag)

    i = 0
    while i < len(text):
        # find next open tag
        oi = text.find(open_tag, i)
        if oi == -1:
            return None
        # check if inside a fence
        # scan from start to oi to track fences
        fence = None
        line_start = 0
        in_block = False
        j = 0
        while j < oi:
            if text[j] == '\n':
                line = text[line_start:j]
                m = FENCE_RE.match(line)
                if m:
                    delimiter = m.group(1)
                    if fence is None:
                        fence = delimiter
                    elif delimiter[0] == fence[0] and len(delimiter) >= len(fence):
                        fence = None
                line_start = j + 1
            j += 1
        if fence is not None:
            # tag inside fence, skip
            i = oi + open_len
            continue

        # find close tag
        ci = text.find(close_tag, oi + open_len)
        if ci == -1:
            return None
        # check close tag not inside fence
        fence = None
        line_start = 0
        j = 0
        while j < ci:
            if text[j] == '\n':
                line = text[line_start:j]
                m = FENCE_RE.match(line)
                if m:
                    delimiter = m.group(1)
                    if fence is None:
                        fence = delimiter
                    elif delimiter[0] == fence[0] and len(delimiter) >= len(fence):
                        fence = None
                line_start = j + 1
            j += 1
        if fence is not None:
            i = ci + close_len
            continue

        return (oi, ci + close_len)
    return None


def strip_context_blocks(text, tag='claude-mem-context'):
    """Remove all <tag>...</tag> blocks from text."""
    open_tag = f'<{tag}>'
    close_tag = f'</{tag}>'
    open_len = len(open_tag)
    close_len = len(close_tag)

    result = []
    i = 0
    while i < len(text):
        oi = text.find(open_tag, i)
        if oi == -1:
            result.append(text[i:])
            break
        ci = text.find(close_tag, oi + open_len)
        if ci == -1:
            result.append(text[i:])
            break
        result.append(text[i:oi])
        i = ci + close_len
    return ''.join(result)


def inject_context_block(text, tag, content, header=None):
    """Replace existing <tag>...</tag> block or append one.
    If header is given and no block exists, prepend header then block.
    Returns new text."""
    open_tag = f'<{tag}>'
    close_tag = f'</{tag}>'
    block = f'{open_tag}\n{content}\n{close_tag}'

    range_ = find_context_block_range(text, tag)
    if range_:
        start, end = range_
        new_text = text[:start] + block + text[end:]
    else:
        if header:
            new_text = text.rstrip('\n') + '\n\n' + header + '\n\n' + block + '\n'
        else:
            new_text = text.rstrip('\n') + '\n\n' + block + '\n'
    return new_text


if __name__ == '__main__':
    # quick test
    test_text = '''Some intro text.

<claude-mem-context>
line one
```
<claude-mem-context> inside fence
```
line two
</claude-mem-context>

Trailing text.
'''
    print('find:', find_context_block_range(test_text))
    print('strip:', strip_context_blocks(test_text))
    print('inject:', inject_context_block(test_text, 'claude-mem-context', 'replaced content'))