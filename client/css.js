export default {
  navbar: {
    outer: 'p-4 flex justify-between items-center bg-gray-100',
    brand: 'mr-2 font-bold text-blue-700 text-3xl',
  },
  modal: {
    outer:
      'fixed w-full h-full top-0 left-0 flex items-center justify-center z-50 p-8',
    mask: 'absolute w-full h-full cursor-pointer bg--text opacity-25',
    content:
      'p-4 bg--bg mx-auto rounded shadow-lg z-50 overflow-y-auto max-h-full',
  },
}
