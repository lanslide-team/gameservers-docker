FROM wine
LABEL maintainer="LAN-slide"

# Reference: https://docs.google.com/spreadsheets/d/14zPsXCGRWkIb42XTa6GxDkMw0cSzNZxgbp7_o66GYJ8/edit#gid=797069815

RUN useradd -m steam && mkdir /wreckfest && chown steam:steam /wreckfest

USER steam
WORKDIR /wreckfest

COPY --chown=steam:steam data ./
COPY --chown=steam:steam entrypoint.sh ./
COPY --chown=steam:steam server_config.cfg ./

RUN chmod +x entrypoint.sh
ENTRYPOINT ./entrypoint.sh

