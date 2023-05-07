#!/usr/bin/env bash
uwsgi --socket 192.168.1.16:8080 --protocol=http --module wsgi --callable app --enable-threads