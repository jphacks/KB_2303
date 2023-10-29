import React from 'react'
import { useState } from 'react';
import { IconView, NameView, Root, UserListView, UserView, DateView } from './Styles'
import { Avater } from '../Avater';

type Props = {
  userListViewInfo:{
    name:string;
    date:Date;
    action: () => void;
  }[]
}

function convertDateToStr(date:Date){
  return date.toLocaleDateString()
}

export const UserList: React.FC<Props> = ({userListViewInfo}) => {
  const [onClick, setOnClick] = useState(0);
	const [hover, setHover] = useState(0);
  return (
    <Root>
      <UserListView>
        {userListViewInfo.map((user) => {
            const iconIndex = userListViewInfo.indexOf(user)+1;
            const dateStr = convertDateToStr(user.date);
            return(
              <UserView 
              key={user.name} 
              onMouseEnter={() => setHover(iconIndex)} 
              onMouseLeave={() => setHover(0)} 
              onClick={() => {setHover(0), setOnClick(iconIndex), user.action()}}>
                <IconView>
                  <Avater name={user.name} size={24}></Avater>
                </IconView>
                <NameView>{user.name}</NameView>
                <DateView>{dateStr}</DateView>
              </UserView>
            )
          })}
        <UserView></UserView>
      </UserListView>
    </Root>
  )
}
