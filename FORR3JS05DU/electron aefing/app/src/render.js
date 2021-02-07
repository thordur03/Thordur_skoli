const videoElement = document.querySelector('video');
const startBtn = document.querySelector('startBtn');
const stopBtn = document.querySelector('stopBtn');

const videoSelectBtn = document.querySelector('videoSelectBtn');




const { desktopCapturer, remote} = require("electron");
const  {Menu} = remote;

async function getVideoSources() {
    const inputSources = await desktopCapturer.getSources({
        types: ["window","screen"]
    });

    const videoOptionsMenu = Menu.buildFromTemplate(
        inputSources.map(source => {
            return {
                label: source.name,
                click: () => selectSource(source)
            }
        })
    );

    videoOptionsMenu.popup();
}

videoSelectBtn.onClick = getVideoSources;
