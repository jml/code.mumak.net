# Notes on deployment

* Statically generated via [pelican](http://getpelican.com/).
* Hosted on S3
* DNS done with cloudfront

## Rough steps

Create S3 bucket for `jml.io` that is configured as a static website.

Upload blog.

Create Cloudfront for the s3 bucket (NB: use the full DNS name, not the one
they suggest).

Wait until that's deployed.

Configure DNS for `jml.io` to point to the cloudfront domain. (A record)

Create S3 buckets for

* jonathanlange.com
* jonathanlange.net
* jonathanlange.org
* mumak.io
* www.jml.io

That are all configured to redirect to `jml.io`

Configure DNS for all of these domains to point to their S3 buckets.
