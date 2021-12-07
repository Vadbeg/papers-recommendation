import {AppBar} from "@mui/material";
import Logo from "./Logo";
import Search from "./components/Search";
import PapersListing from "./components/PapersListing";
import {Link, useSearchParams} from "react-router-dom";

function PapersPage(props) {
    return (
        <div>
            <AppBar
                style={{
                    padding: 10,
                    fontSize: 25,
                    display: 'flex',
                    flexDirection: 'row',
                    height: 70,
                }}
                >
                <Link to="/" style={{ textDecoration: 'none' }}>
                    <Logo style={{marginLeft: 10, marginTop: 5}}/>
                </Link>
                <Search style={{marginLeft: '70%'}}/>
            </AppBar>
            <PapersListing similar={props.similar}/>
        </div>
    )
}

export default PapersPage