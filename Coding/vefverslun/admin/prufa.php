<!DOCTYPE html>
<html>
<head>
  <style>
    @font-face {
      font-family: 'customFont';
      src: url('font/Eastwood.woff2') format('woff2'), /* WOFF2 format */
           url('font/Eastwood.woff') format('woff'), /* WOFF format */
           url('font/Eastwood.ttf') format('truetype'); /* TTF format */
    }

    .custom-text {
      font-family: 'customFont', sans-serif;
    }
  </style>
</head>
<body>
  <p class="custom-text">This text will use the custom font.</p>
</body>
</html>