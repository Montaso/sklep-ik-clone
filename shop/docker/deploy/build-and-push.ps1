param (
	[string]$Arg1	# img tag
)

docker build -t sklepik-prestashop-deploy:latest -f presta.deploy.dockerfile ./../../..
./push-image.ps1 sklepik-prestashop-deploy $Arg1