import Logo from "./Logo";
import Search from "./components/Search";

function WelcomePage() {
    return (
        <div style={{
            backgroundColor: '#282c34',
            minHeight: '100vh',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 'calc(10px + 2vmin)',
            color: 'white',
        }}>
            <Logo style={{fontSize: 60}}/>
            <Search style={{marginTop: 50}}/>
        </div>
    )
}

export default WelcomePage