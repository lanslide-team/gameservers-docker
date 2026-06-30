FROM wine
LABEL maintainer="LAN-slide"

# Reference: https://docs.google.com/spreadsheets/d/14zPsXCGRWkIb42XTa6GxDkMw0cSzNZxgbp7_o66GYJ8/edit#gid=797069815

RUN useradd -m steam && mkdir -p /wreckfest2 /wreckfest2/save /compat && chown steam:steam /wreckfest2 /wreckfest2/save /compat

ENV XDG_RUNTIME_DIR=/tmp/runtime-steam
RUN mkdir -p "$XDG_RUNTIME_DIR"
RUN chmod 700 "$XDG_RUNTIME_DIR"
RUN chown steam "$XDG_RUNTIME_DIR"

USER steam
WORKDIR /wreckfest2

COPY --chown=steam:steam data ./
COPY --chown=steam:steam entrypoint.sh ./
COPY --chown=steam default_loop.becl /wreckfest2/save/default_loop.becl
COPY --chown=steam server_config.scnf /wreckfest2/save/server_config.scnf

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

