param (
	[string]$Arg1
	[string]$Arg2
)

docker login
docker tag $Arg1 arivaldi/sklepik-prestashop:$Arg2
docker push arivaldi/sklepik-prestashop:$Arg2
