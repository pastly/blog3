---
title: "I Wrote a Brainfuck Interpreter (in Rust)"
date: 2021-01-08
slug: 2021-01-08-i-wrote-a-brainfuck-interpreter-in-rust
type: posts
draft: false
categories:
  - default
tags:
  - brainfuck
  - rust
---

*This post first appeared on my old blog in January 2021. It is preserved,
but maybe not updated, here.*

---

[repo]: https://github.com/pastly/brainfuck-rs

The repo is on Github [here][repo], and in case that turns out to be a lie in
the future, the code as of the initial writing of this post is
[here](/brainfuck-rs.txz).

# About brainfuck

Brainfuck is an esoteric programming language with only eight commands (i.e.
it's meant to be fun/challenging, not useful). Memory is represented as cells
on an infinitely long tape and accessed with a single pointer. Typically each
cell is a single byte, and by convention "infinitely long" means 30,000 cells.
The eight commands are:

1. `>` move cell pointer to the right,
2. `<` move cell pointer to the left,
3. `+` increment value in current cell,
4. `-` decrement value in current cell,
5. `[` enter loop if current cell value is not 0, else jump to end,
6. `]` end loop,
7. `,` accept one byte of input and store in current cell,
8. `.` output byte in current cell.

All other characters in brainfuck source code are comments.

As an example, the following program writes "Hello World!" followed by a
newline to stdout.

    ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.++
    +.------.--------.>>+.>++.

# Thoughts

Writing an interpreter and checking that other people's brainfuck programs run
in it was a lot easier than actually learning brainfuck and writing it. That
said, I do want to learn it well enough to write some simple things.

There are a couple simple optimizations I'd like to try implementing that are
documented in the README. The most obvious is to coalesce repeated
instructions. I intend on writing a script to measure the improvement these
optimizations have.

# Brainfuck resources on the web

<https://en.wikipedia.org/wiki/Brainfuck>

<http://brainfuck.org/>

<https://github.com/fabianishere/brainfuck>
