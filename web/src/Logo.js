const ratio = 5/14

function Logo(props) {
    const fontSize = props.style?.fontSize || 25
    const width = fontSize / ratio
    return (
        <div style={{
            ...props.style,
            fontFamily: 'MeowScript',
            color: 'white',
            width: width, lineHeight: 0.5,
            alignItems: 'normal'
        }}>
            <div style={{textAlign: 'left'}}>Wipe</div>
            <div style={{textAlign: 'right'}}>with</div>
            <div style={{textAlign: 'left'}}>paper</div>
        </div>
    )
}

export default Logo
