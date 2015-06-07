Status: draft
Title: How programming language affects my approach

## Introduction

For a while I've suspected when I solve a problem using Haskell, I do so in a
different manner than I'd solve the same problem in Python.

I don't know if this is a real thing, and I don't know what causes it, but I
thought it might be worth exploring. Here's the exploration.

## The problem

I've got a command-line todo list application in the works. It's in Haskell.

At this stage, I've got most of the core functionality written up, but I'd
like to change the way the tool is configured. Currently, it has a couple of
command line options, with hard-coded defaults. I'd like to be able to
configure the tool with a configuration file.

## Requirements

* Configuration file in YAML
* Sensible default location for configuration file (e.g.
  `~/.todo/config.yaml`)
* Overwrite configuration file location with command-line option (e.g. `-d
  ~/todo/diff-config.yaml`)
* Overwrite most configuration file settings with command-line options
* Paths in the configuration file can use `~` to refer to the user's home
  directory

## Current set up

I have a `Config` data record and a `defaultConfig` instance of that record
with some defaults.

I use the [GetOpt](XXX) package to parse command-line options. I use the
result of that parsing to update the `defaultConfig` instance with
user-specified values.

## If it were Python I'd

* find a YAML parsing library
* start by loading from a hard-wired location
* change the 
