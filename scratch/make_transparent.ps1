# Load System.Drawing assembly from .NET
Add-Type -AssemblyName System.Drawing

# Path to the logo image
$imagePath = ".\public\assets\img\logo-change.png"

Write-Output "Loading logo from $imagePath ..."

if (Test-Path $imagePath) {
    # Load bitmap
    $bmp = New-Object System.Drawing.Bitmap($imagePath)
    
    Write-Output "Image loaded successfully. Size: $($bmp.Width)x$($bmp.Height)"
    
    # Define white color to make transparent
    # Standard white is R=255, G=255, B=255
    $whiteColor = [System.Drawing.Color]::FromArgb(255, 255, 255)
    
    # Make all white pixels transparent
    $bmp.MakeTransparent([System.Drawing.Color]::White)
    
    # Save back in PNG format
    $bmp.Save($imagePath, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
    
    Write-Output "Successfully removed background! Saved transparent logo to $imagePath"
} else {
    Write-Error "Logo file not found at $imagePath"
}
