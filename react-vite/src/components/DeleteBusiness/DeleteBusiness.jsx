import React from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch } from 'react-redux';
import { deleteBusinessThunk } from '../../redux/business';
import './DeleteBusiness.css';


export default function DeleteBusiness({busId}) {

  const {closeModal} = useModal()
  const dispatch = useDispatch()

  const handleSubmit = async() => {
    await dispatch(deleteBusinessThunk(busId))
    closeModal()
  }

  return (
    <div id='delete-business-container'>
      <h1 className='title'>Delete this business?</h1>
      <div className='buttons-container'>
        <button id='yes-btn' onClick={handleSubmit}>YES</button>
        <button id='no-btn' onClick={closeModal}>NO</button>
      </div>
    </div>
  )
}
