VERSION=1.1

echo -e "#####################################\n\n"

echo -e "Starting building process....\n\n"

echo -e "#####################################"

docker buildx create --name multi_scheduler

docker buildx use multi_scheduler

docker buildx build --platform linux/arm/v6,linux/amd64,linux/arm64,linux/arm/v7 -t mariospapaz/uni_scheduler:${VERSION} --push .
