import React from 'react'

function HelloWorld() {
  const [number, setNumber] = React.useState(0)
  return (
    <div>
      <h1>Hello World! {number} times!</h1>
      <button onClick={() => setNumber(number + 1)}>Click me!</button>
    </div>
  )
}

export default HelloWorld // Defines which component will be rendered as an entrypoint.
