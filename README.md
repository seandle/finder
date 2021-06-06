# Finder
Find your server IP using Tor and Crypto

## Installing
```
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Development
```
(venv) $ export FLASK_APP=app
(venv) $ flask run
```

## Production

### Nginx config sample
```
upstream onion {
    server 127.0.0.1:80;
}


server {
    listen       127.0.0.1:80;
    server_name  ddrkevl3efqwltimx4yc2d2rqcbkj4y5gug6lu4r6r6pxmggr3la5gyd.onion;
    allow 127.0.0.1;
    deny all;
    server_tokens off;
    location / {
        proxy_pass http://localhost:8095/;
    }
}

```
### Docker Compose sample
```

```

### Tor setup
```

```

