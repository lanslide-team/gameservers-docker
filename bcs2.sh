
docker build -t='counter-strike-sharp:latest' counter-strike-sharp/ --no-cache
docker build -t='cs2-vanilla:latest' cs2-vanilla/ --no-cache
docker build -t='cs2-comp:latest' cs2-comp/ --no-cache
docker build -t='cs2-wingman:latest' cs2-wingman/ --no-cache

docker image prune -f
