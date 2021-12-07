import {Button, Paper, Typography, useTheme} from "@mui/material";
import {useNavigate} from "react-router-dom";

function PaperComponent(props) {
    const navigate = useNavigate()
    const theme = useTheme()
    const {title, abstract, id} = props.paper
    return (
        <Paper
            elevation={8}
            style={{
                marginBottom: 50,
                // color: theme.palette.primary,
            }}
            onClick={() => {
                navigate(`/papers/${id}`)
            }}
        >
        <Button style={{
            color: 'black',
            flexDirection: 'column',
            padding: 15,
            textTransform: 'none'
        }}>
                <Typography variant="h4">{title}</Typography>
                <div style={{
                    textAlign: 'left',
                    fontSize: 11,
                }}>{abstract}</div>
        </Button>
        </Paper>
    )
}

export default PaperComponent