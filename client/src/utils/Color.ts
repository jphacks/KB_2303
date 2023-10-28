export const Color = {
  gray: {
    [100]: '#FCFCFC',
    [150]: '#F5F5F5',
    [200]: '#EFEFEF',
    [300]: '#DFDFDF',
    [400]: '#B7B7B7',
    [600]: '#777777',
    [850]: '#1F1F1F',
    [900]: '#111111',
  },
  navy: {
    [400]: '#C8CFDC',
    [900]: '#202A43',
  },
  white: '#ffffff',
  black: '#000000',
  green: {
    main: '#06C755',
    active: '#1E6E1E',
  },
  red: {
    main: '#FF334B',
    active: '#C9162B',
  },
}

export const hex2rgb = (hex: string) => {
  return hex2rgba(hex, 1)
}

export const hex2rgba = (hex: string, alpha: number) => {
  const arr = [hex.slice(1, 3), hex.slice(3, 5), hex.slice(5, 7)].map((str) =>
    parseInt(str, 16)
  )
  return `rgb(${arr[0]} ${arr[1]} ${arr[2]} / ${alpha})`
}