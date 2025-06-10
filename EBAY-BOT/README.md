# EBAY-BOT

To enable remote debugging for Chrome (required for this project), run:

```sh
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome-debug"
```

This will start Chrome with the necessary debugging options.

## Publishing Ads

To publish your ads, run:

```sh
./kleinanzeigen-bot publish
```

To force publishing, add the `--force` flag:

```sh
./kleinanzeigen-bot publish --force
```