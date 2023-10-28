import React from 'react'

type Props = {
  color: string
  size: number
}

export const UserIcon: React.FC<Props> = ({ color, size }) => {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 48 48"
      fill="none"
      xmlns="http://www.w3.org/2000/svg">
      <mask maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48">
        <rect width="48" height="48" fill="#D9D9D9" />
      </mask>
      <g mask="url(#mask0_11_2175)">
        <path
          d="M24 24C21.8 24 19.9167 23.2167 18.35 21.65C16.7833 20.0833 16 18.2 16 16C16 13.8 16.7833 11.9167 18.35 10.35C19.9167 8.78333 21.8 8 24 8C26.2 8 28.0833 8.78333 29.65 10.35C31.2167 11.9167 32 13.8 32 16C32 18.2 31.2167 20.0833 29.65 21.65C28.0833 23.2167 26.2 24 24 24ZM8 40V34.4C8 33.2667 8.29167 32.225 8.875 31.275C9.45833 30.325 10.2333 29.6 11.2 29.1C13.2667 28.0667 15.3667 27.2917 17.5 26.775C19.6333 26.2583 21.8 26 24 26C26.2 26 28.3667 26.2583 30.5 26.775C32.6333 27.2917 34.7333 28.0667 36.8 29.1C37.7667 29.6 38.5417 30.325 39.125 31.275C39.7083 32.225 40 33.2667 40 34.4V40H8Z"
          fill={color}
        />
      </g>
    </svg>
  )
}
