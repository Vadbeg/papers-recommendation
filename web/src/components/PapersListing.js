import PaperComponent from './PaperComponent'
import {useEffect, useState} from 'react'
import {LinearProgress, Paper, Typography, useTheme} from "@mui/material";
import papers_mock from './similiar_mock.json'
import {useNavigate, useParams, useSearchParams} from "react-router-dom";
import superagent from 'superagent'
import {useStore} from "../store";

const API_URL = `http://localhost:8000`

function PapersListing(props) {
    const theme = useTheme()

    const [store, setStore] = useStore()
    const papers = store.papers
    const setPapers = papers => setStore(s => ({...s, papers}))

    const [similarPapers, setSimilarPapers] = useState([])

    const navigate = useNavigate()

    const [searchParams] = useSearchParams()
    const {paper_id: paperId} = useParams()

    const query = searchParams.get('query')

    const [loading, setLoading] = useState(false)

    useEffect(async () => {
        if (query) {
            setLoading(true)
            const {body: papers} = await superagent
                .get(`${API_URL}/papers`)
                .query({query})
                .catch(err => {
                    alert(err)
                    navigate('/')
                })
            await superagent
                .get(`${API_URL}/train`)
                .catch(err => {
                    alert(err)
                    navigate('/')
                })
            setPapers(papers)
            setLoading(false)
        }
    }, [query])

    useEffect(async () => {
        if (paperId) {
            setLoading(true)
            const {body: similarPapers} = await superagent
                .get(`${API_URL}/similar`)
                .query({paper_id: paperId})
                .catch(err => {
                    alert(err)
                    navigate('/')
                })
            setLoading(false)
            setSimilarPapers(similarPapers)
        }
    }, [paperId])

    return (
        <Paper
            elevation={4}
            style={{
                margin: 50,
                padding: 50,
                backgroundColor: theme.palette.secondary,
            }}
        >
            {loading && <LinearProgress />}
            {!loading && paperId &&
            <div>
                <Typography
                    variant="h4"
                    style={{marginBottom: 30}}
                >
                    Similar to "{papers.find(p => p.id === paperId).title}":
                </Typography>
                {similarPapers
                    .filter(p => p.paper_dist !== 0)
                    .sort((p1, p2) => p1.paper_dist - p2.paper_dist)
                    .map(p => <PaperComponent paper={p} key={p.id}/>)
                }
            </div>
            }
            {!loading && !paperId && papers.map(p => <PaperComponent paper={p} key={p.id}/>)}
        </Paper>
    )
}

export default PapersListing