import {Button, TextField, useTheme} from "@mui/material";
import {useEffect, useRef, useState} from "react";
import {useNavigate, useSearchParams} from "react-router-dom";

function Search(props) {
    const [text, setText] = useState('')
    const navigate = useNavigate()
    const [searchParams] = useSearchParams()
    const query = searchParams.get('query')
    useEffect(() => {
        query && setText(query)
    }, [query])

    const buttonRef = useRef(null)

    return (
        <div style={{
            ...props.style,
            display: 'flex',
            flexDirection: 'row',
            maxHeight: 50
        }}>
            <TextField
                label="Query"
                variant="filled"
                InputProps={{style:{
                    height: 50,
                    backgroundColor: 'white'
                    // color: 'white'
                }}}
                onChange={e => setText(e.target.value)}
                value={text}
                onKeyUp={(e) => {
                    if(e.keyCode === 13){
                        buttonRef.current.click();
                    }
                }}
            />
            <Button
                variant="filled"
                style={{
                    backgroundColor: '#5e85a5',
                    marginLeft: 10,
                }}
                onClick={() => {
                    navigate(`/papers?query=${text}`)
                }}
                ref={buttonRef}
            >
                Search
            </Button>
        </div>
    )
}

export default Search