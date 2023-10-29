import React from 'react'
import { useState } from 'react';
import { IconList, NavigationIcon, Root } from './Styles'
import { Icon } from '../Icon';
import { Color } from '../../utils/Color';

type Props = {
  navigations:{
    icon:string;
    action: () => void;
  }[]
  
}



export const Navigater: React.FC<Props> = ({navigations}) => {
  const [onClick, setOnClick] = useState(0);
	const [hover, setHover] = useState(0);
  return (
    <Root>
      <IconList>
          {navigations.map((navigate) => {
            const iconIndex = navigations.indexOf(navigate)+1;
            return(
              <NavigationIcon 
              key={navigate.icon} 
              onMouseEnter={() => setHover(iconIndex)} 
              onMouseLeave={() => setHover(0)} 
              onClick={() => {setHover(0), setOnClick(iconIndex), navigate.action()}}>
                <Icon 
                color={(onClick === iconIndex) ? Color.white : (hover === iconIndex) ? Color.gray[300] :Color.navy[400]} 
                size={48}>{navigate.icon}</Icon>
              </NavigationIcon>
            )
          })}
      </IconList>
    </Root>
  )
}
