param (
	[string]$Arg1, 	# img name
	[string]$Arg2	# img tag
)

docker login
docker tag $Arg1 arivaldi/sklepik-prestashop:$Arg2
docker push arivaldi/sklepik-prestashop:$Arg2
