function getAverageColor(imageElement, ratio){
    const canvas = document.createElement("canvas");

    let height = canvas.height = imageElement.width;
    let width = canvas.width = imageElement.height;

    const context = canvas.getContext("2d")
    context.drawImage(imageElement, 0, 0)

    let data, length;
    let i = -4, count = 0

    try{
        data = context.getImageData(0, 0, width, height)
        length = data.data.length
    } catch (err){
        console.error(err)
        return{
            R: 0,
            G: 0,
            B: 0,
        }
    }

    let R,G,B
    R = G = B = 0

    while((i += ratio * 4) < length){
        ++count

        R+= data.data[i]
        G+= data.data[i +1]
        B+= data.data[i +2]
    }

    R = ~~(R/ count)
    G = ~~(G/ count)
    B = ~~(B/ count)

    return {
        R, G, B
    }

}

const image = document.querySelector("img")
const container = document.querySelector(".products_container")

image.onload = function(){
    
    const {R,G,B} = getAverageColor(image, 4)

    const colors = [R,G,B]
    
    let style = `linear-gradient(-20deg, rgb(${R}, ${G}, ${B}), rgb(${R+(B*2/3)}, ${G+(R*2/3)}, ${B+(G*2/3)}))`;
    container.style.backgroundImage = style;
}

