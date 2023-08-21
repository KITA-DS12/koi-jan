# loveMahjong

起動
```
docker-compose up
```

起動(background)
```
docker-compose up -d
```

停止
```
docker-copose down
```

serverのみ起動
```
dokcer-compose up server
```

clientのみ起動
```
dokcer-compose up client
```
psqlを起動
```
docker exec -it koi-jan_db_1 bash
psql -U root -d koijan
```
