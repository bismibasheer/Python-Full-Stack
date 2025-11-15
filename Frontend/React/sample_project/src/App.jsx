
import Navbar from "./Components/Navbar/Navbar"
import Home from "./Components/Pages/Home/Home"
import Register from "./Components/Pages/Register/Register"
import All_Movies from "./Components/ALL MOVIES/All_Movies"
import Dashboard from "./Components/Dashboard/Dashboard"
import Editprofile from "./Components/Dashboard/Editprofile"
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Layout from "./Components/Dashboard/Layout"
import Counter from "./Components/Counter"
function App() {


  return (
    <>
  <div>
    <BrowserRouter>
    <Navbar/>
    {/* <Counter/> */}
    <Routes>
    
    <Route path="/" element={<Home/>}/>
    <Route path="/register" element={<Register/>}/>
    <Route path="/all_movies" element={<All_Movies/>}/>
    <Route path="/dashboard" element={<Layout/>}>
       <Route index element={<Dashboard/>}/>
       <Route path="editprofile" element={<Editprofile/>}/>
       </Route>
    <Route path="/counter" element={<Counter/>}/>

    </Routes>
    </BrowserRouter>
  </div>
  </>
  )
}

export default App
