#!/bin/sh
set -eu
test "$(cat src/greeting.txt)" = "annyeong"
