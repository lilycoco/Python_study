<!DOCTYPE html>

<html>
  <body>
    <h1>Bot App</h1>
    <form method="post" action="/hello">
      Please input: <input type="text" name="input_text">
      <input type="submit" value="send">
    </form>
    <ul>
    <li>msg: {{input_text}}</li>
    <li>response: {{output_text}}</li>
    </ul>
  </body>
</html>