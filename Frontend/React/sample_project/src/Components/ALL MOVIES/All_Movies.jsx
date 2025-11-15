import { useState ,useEffect } from "react"
import "./all_movies.css"
import Card from "./card"
import axios from 'axios'

function All_Movies() {
  const [movies,setMovies]=useState([])
  const [text,setText]=useState("spiderman")
    useEffect(()=>{
     
      
    },[])
     
      // {
      //   "#TITLE": "Spider-Man",
      //   "#YEAR": 2002,
      //   "#IMDB_ID": "tt0145487",
      //   "#IMG_POSTER": "https://m.media-amazon.com/images/M/MV5BZWM0OWVmNTEtNWVkOS00MzgyLTkyMzgtMmE2ZTZiNjY4MmFiXkEyXkFqcGc@._V1_.jpg",
      // },
      // {
      //   "#TITLE": "Spiderman the Verse",
      //   "#YEAR": 2019,
      //   "#IMDB_ID": "tt12122034",
      //   "#IMG_POSTER": "https://m.media-amazon.com/images/M/MV5BNDBjNWY3OWYtMjk2ZS00NjA2LWE0NzAtOWQxNzBhNjZlMGYyXkEyXkFqcGc@._V1_.jpg",
      // } , 
      

     const handleSearch=()=>{
      axios.get(`https://imdb.iamidiotareyoutoo.com/search?q=${text}`)
      .then((response)=>{
        console.log(response.data.description)
        setMovies(response.data.description)
      })
  }

    return (
      <>
        <h1>All Movies</h1>
       
        <div style={{margin:"50px 10px"}}> 
        <input type='text' name="search" value={text} onChange={(e)=>setText(e.target.value)}/>
        <button onClick={handleSearch}>Search</button>
      </div>




        <div className="movie-section">
          {
            movies.map((cinema)=>(
            <Card key={cinema["#IMDB_ID"]} title={cinema["#TITLE"]} poster={cinema["#IMG_POSTER"]}/>
            ))
          }
        </div>
        
      
      </>

    
    )
  }


export default All_Movies
