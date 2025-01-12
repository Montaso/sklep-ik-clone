param (
	[string]$Arg1
)

docker login
docker tag shop-prestashop arivaldi/sklepik-prestashop:$Arg1
docker push arivaldi/sklepik-prestashop:$Arg1
