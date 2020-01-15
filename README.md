# Memobird Subscriptions

## Feature

- Rainning notification
- Quote of the day

## Usage

`docker run -e AK=YOUR_ACCESS_KEY -e DEVICE_ID=YOUR_DEVICE_ID -e CAIYUN_TOKEN=YOUR_CAIYUN_API_TOKEN -e CAIYUN_LOCATION=YOUR_LOCATION -it --rm tevino/memobird-subscriptions`

- YOUR_LOCATION

The format is `longitude,latitude` e.g. `121.6544,25.1552`, as specified [here][CAIYUN_API]

[CAIYUN_API]: https://open.caiyunapp.com/%E5%AE%9E%E5%86%B5%E5%A4%A9%E6%B0%94%E6%8E%A5%E5%8F%A3/v2.2
