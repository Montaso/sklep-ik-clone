param (
	[string]$Arg1
)

docker build -t sklepik-prestashop-deploy:$Arg1 -f presta.deploy.dockerfile ./../../..
./push-image.ps1 sklepik-prestashop-deploy $Arg1