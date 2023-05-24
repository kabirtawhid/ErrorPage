import React from 'react';
import { useNavigate, useRouteError } from 'react-router-dom';

const ErrorPage = () => {
  const error = useRouteError();
  console.error(error);
  const navigate = useNavigate();

  return (
    <div id='error-page' className='flex flex-col justify-center items-center h-screen' >
      <h1 className='text-center text-9xl font-extrabold'>{error.status}</h1>
      <p className='mt-4 text-4xl text-gray-600 font-semibold'>
        <i>{error.statusText || error.message}</i>
      </p>
      <p>
        <button onClick={() => navigate(-1)} className='bg-blue-500 rounded-lg text-white font-extrabold px-7 py-3 mt-7'>Go Back</button>
      </p>
    </div>
  );
};

export default ErrorPage;