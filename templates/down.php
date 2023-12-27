<?php
$path = 'test.zip';
if (!file_exists($path)) {
   echo 'ErrOr 404';
}
  $size = filesize($path);
  header('Content-Type: application/zip');
  header('Content-Length: ' . $size);
  header('Content-Dispsition: Attachment; FileName="' . $path . '"');
  readfile($path);
}
?>
<!doctype html>
<html>
<head>
   <title>Download</title>
</head>
<body>
<h1>Спачибо за скачивание</h1>
</body>
</html>
