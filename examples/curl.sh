#!/usr/bin/env bash
# Pinterest API 的 curl 示例：所有能力都发到同一个地址，只换 action 和 params。
# curl examples for the Pinterest API: every capability uses the same URL; only action and params change.
#
#   export EVERYINFRA_API_KEY=<your API key>
#   bash examples/curl.sh search "camping gear"
#   bash examples/curl.sh profile rei           # 账号短名 / a username
#   bash examples/curl.sh user_posts rei
#   bash examples/curl.sh pin "<pin url>"       # pins 结果里的 url / the url from a pins result
#   bash examples/curl.sh boards rei
set -euo pipefail
: "${EVERYINFRA_API_KEY:?Set EVERYINFRA_API_KEY first: https://everyinfra.com/docs#quickstart}"
action=${1:?"usage: bash examples/curl.sh <search|profile|user_posts|pin|boards> <value>"}
value=${2:?"value: a keyword, a pin url or a username"}

case "$action" in
  search)                        params="{\"keyword\":\"$value\"}" ;;
  profile | user_posts | boards) params="{\"username\":\"$value\"}" ;;
  pin)                           params="{\"url\":\"$value\"}" ;;
  *) echo "unknown action: $action (use search, profile, user_posts, pin or boards)" >&2; exit 2 ;;
esac

curl -sS -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"platform\":\"pinterest\",\"action\":\"$action\",\"params\":$params}"
echo
