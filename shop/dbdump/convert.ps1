param (
	[string]$Arg1
)

(Get-Content $Arg1) -replace 'utf8mb4_0900_ai_ci', 'utf8mb4_general_ci' | Set-Content $Arg1