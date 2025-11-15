import { useState } from "react"

function Counter() {
    const [count,setCount]=useState(0);
    
    function Increment(){
        setCount(count+1)
    }

    function Decrement(){
        setCount(count-1)
    }
 

    return (
        <div>
        {count}
        <button onClick={Increment}>Increment</button>
        <button onClick={Decrement}>Decrement</button>
        </div>
  )
}

export default Counter
