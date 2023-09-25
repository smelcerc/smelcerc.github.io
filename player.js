kalturaPlayer.addEventListener(kalturaPlayer.Event.PLAY, (event) => {
                     console.log('PLAY started');   
                     function delay(time) {
                      return new Promise(resolve => setTimeout(resolve, time));
                    }
                    async function hideCaptions() {
                      kalturaPlayer.hideTextTrack();
                      await delay(2000);
                      kalturaPlayer.showTextTrack();
                    }
                    async function handleCaptions(){
                      const playerTracks = kalturaPlayer.getActiveTracks();
                      console.log(playerTracks.text._label);
                      if (playerTracks.text._label != 'Off'){
                        hideCaptions();
                      }
                    }
                    handleCaptions();
                  }
                  );