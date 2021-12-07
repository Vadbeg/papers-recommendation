import './App.css';
import {createTheme, ThemeProvider} from "@mui/material";
import WelcomePage from "./WelcomePage";
import PapersPage from "./PapersPage";
import {BrowserRouter, Route, Routes} from "react-router-dom";

function App() {
    const theme = createTheme({
        palette: {
            primary: {
                main: '#282c34'
            },
            background: {
                main: 'white'
            }
        }
    })
    return (
        <ThemeProvider theme={theme}>
            <BrowserRouter>
                <Routes>
                    <Route path="/">
                        <Route index element={<WelcomePage />} />
                        <Route path="papers" element={<PapersPage />}>
                            <Route path=":paper_id" element={<PapersPage/>} />
                        </Route>
                    </Route>
                </Routes>
            </BrowserRouter>
        </ThemeProvider>
    );
}

export default App;
