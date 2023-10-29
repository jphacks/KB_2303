import React from 'react'
import { useState } from 'react';
import {
  IconView,
  NameView,
  Root,
  UserListView,
  UserView,
  DateView,
} from './Styles'
import { Avater } from '../Avater'

type Props = {
  userListViewInfo: {
    name: string
    date: Date
    action: () => void
  }[]
  selectedItem: string
}

function convertDateToStr(date: Date) {
  return date.toLocaleDateString()
}

export const UserList: React.FC<Props> = ({
  userListViewInfo,
  selectedItem,
}) => {
  return (
    <UserListView>
      {userListViewInfo.map((user) => {
        const dateStr = convertDateToStr(user.date)
        return (
          <UserView
            key={user.name}
            isSelected={user.name === selectedItem}
            onClick={user.action}>
            <IconView>
              <Avater name={user.name} size={24}></Avater>
            </IconView>
            <NameView>{user.name}</NameView>
            <DateView>{dateStr}</DateView>
          </UserView>
        )
      })}
    </UserListView>
  )
}
