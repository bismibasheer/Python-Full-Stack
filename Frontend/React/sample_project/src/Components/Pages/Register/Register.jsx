import { useState } from "react"

function Register() {
  const [data,setData]=useState({
    "full_name":"",
    "course":""
  })

  const handleData=(e)=>{
    const {name,value}=e.target;
    setData({...data,[name]:value})
  }

  const handleRegister=(e)=>{
    e.preventDefault() // to prevent page reload
    // Actions to perform after form submit
    console.log(data)
    setData({"full_name":"","course":""})// to set data to initial state
  }
  return (
    <>
        <h1 style={{textAlign:"center",color:"green"}}>Register</h1>
        <form onSubmit={handleRegister}>
          <label>Full name</label>
          <input type="text" name="full_name" value={data.full_name} onChange={handleData}/>
          <br/><br/>
          <label>Course</label>
          <input type="text" name="course" value={data.course} onChange={handleData}/>
          <br/><br/>
          <button type="submit">Register</button>
        </form>
        
    </>

  )
}

export default Register