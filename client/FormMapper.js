import React from 'react'

// TODO this is hard coded now, but the page count and the pdf names could be pulled from the server
const forms = [
  'Narcan Participant Refill Form -2018.pdf',
  'Narcan Participant Training Form - 2018.pdf',
  'Provider Training Form - 201.pdf',
]

const getPages = (s) => [1, 2].map((n) => s + `-${n}.png`)

export const FormMapperPicker = () => {
  return (
    <ul className="list-inside">
      {forms.map((form_name) => (
        <li key={form_name} className="mb-2">
          {form_name}
          {getPages(form_name).map((img_name, i) => (
            <div className="" key={img_name}>
              <a href={img_name}>Page #{i + 1}</a>
            </div>
          ))}
        </li>
      ))}
    </ul>
  )
}

const EntryBox = (props) => {
  const [name, ...xywh] = props.entry
  return (
    <div className="mb-2">
      <input
        className="px-2 py-1 border"
        value={name}
        onChange={props.onChange}
        placeholder={props.placeholder}
      />
      <span className="mx-4">{xywh.join(', ')}</span>
      <i
        className="text-red-500 fa fa-trash cursor-pointer"
        onClick={props.onDelete}
      />
    </div>
  )
}

export default class FormMapper extends React.Component {
  state = {
    entries: [],
  }
  constructor(props) {
    super(props)
    this.storage_key = 'mapper__' + this.props.img_name
    const _entries = window.localStorage.getItem(this.storage_key)
    if (_entries) {
      this.state.entries = JSON.parse(_entries)
    }

    this.canvasRef = React.createRef()
    this.imgRef = React.createRef()
    this.scrollRef = React.createRef()
  }
  imgLoad = () => {
    const { width, height } = this.imgRef.current
    this.setState({ width, height })
    setTimeout(this.draw, 50) // not sure why it isn't drawing on the previous line
  }
  draw = () => {
    const canvas = this.canvasRef.current
    if (!canvas || !this.state.width) {
      return
    }
    const { width, height } = this.state
    canvas.width = width
    canvas.height = height
    const ctx = canvas.getContext('2d')
    ctx.clearRect(0, 0, width, height)
    this.state.entries.forEach((entry, i) => {
      const [name, x, y, w, h] = entry
      ctx.fillStyle = 'rgba(128,255,128,0.5)'
      ctx.fillRect(x, y, w, h)
      ctx.fillStyle = 'black'
      ctx.font = '10px serif'
      ctx.fillText(name || `Item #${i + 1}`, x, y + 10)
    })

    const { click, hover } = this.state
    if (click && hover) {
      ctx.fillStyle = undefined
      ctx.lineWidth = 3
      ctx.strokeStyle = 'black'
      ctx.strokeRect(
        click[0],
        click[1],
        hover[0] - click[0],
        hover[1] - click[1],
      )
    }
    window.localStorage.setItem(
      this.storage_key,
      JSON.stringify(this.state.entries),
    )
  }

  getXY = (e) => {
    const { left, top } = this.canvasRef.current.getBoundingClientRect()
    return [e.clientX - left, e.clientY - top]
  }
  onMouseDown = (e) => this.setState({ error: null, click: this.getXY(e) })
  onMouseMove = (e) =>
    this.state.click && this.setState({ hover: this.getXY(e) })
  onMouseUp = (e) => {
    const { click, entries } = this.state
    let [x0, y0] = click
    let [x1, y1] = this.getXY(e)
    if (x0 > x1) {
      const temp = x0
      x0 = x1
      x1 = temp
    }
    if (y0 > y1) {
      const temp = y0
      y0 = y1
      y1 = temp
    }
    const w = x1 - x0
    const h = y1 - y0
    if (w < 10 || h < 10) {
      this.setState({
        error: 'Cannot make boxes smaller than 10px',
        hover: null,
        click: null,
      })
      setTimeout(() => this.setState({ error: null }), 5000)
      return
    }
    entries.push(['', x0, y0, w, h])
    if (this.scrollRef.current) {
      this.scrollRef.current.scrollTop = this.scrollRef.current.scrollHeight
    }
    this.setState({ hover: null, click: null, entries })
  }
  changeEntry = (i) => (e) => {
    const { entries } = this.state
    entries[i][0] = e.target.value
    this.setState({ entries })
  }
  deleteEntry = (i) => () => {
    const { entries } = this.state
    entries.splice(i, 1)
    this.setState({ entries })
  }
  copy = () => {
    navigator.clipboard.writeText(
      this.state.entries.map((e) => e.join(',')).join('\n'),
    )
    this.setState({ copied: true })
    setTimeout(() => this.setState({ copied: false }), 5000)
  }
  render() {
    const { img_name } = this.props.match.params
    const { width, height, entries, copied, error } = this.state
    this.draw()
    return (
      <div className="relative">
        <img
          src={`/blank_form/${img_name}`}
          className="max-w-none"
          onLoad={this.imgLoad}
          ref={this.imgRef}
        />
        <canvas
          className="absolute top-0 left-0 bottom-0 right-0"
          onMouseDown={this.onMouseDown}
          onMouseMove={this.onMouseMove}
          onMouseUp={this.onMouseUp}
          ref={this.canvasRef}
          height={height}
          width={width}
        />
        <div className="fixed bottom-0 right-0 bg-white p-4 border">
          {entries.length > 0 ? (
            <div>
              <div
                style={{ maxHeight: 200, overflowY: 'auto' }}
                ref={this.scrollRef}
              >
                {entries.map((entry, i) => (
                  <EntryBox
                    key={i}
                    entry={entry}
                    onChange={this.changeEntry(i)}
                    onDelete={this.deleteEntry(i)}
                    placeholder={`Item #${i + 1}`}
                  />
                ))}
              </div>
              <div
                onClick={this.copy}
                className="cursor-pointer text-underline"
              >
                {copied ? 'Copied!' : 'Copy To Clipboard'}
              </div>
            </div>
          ) : (
            <div>Click and drag anywhere to make a box.</div>
          )}
          {error && (
            <div className="p-2 bg-red-200 text-red-600 mt-2">
              <i className="fa fa-exclamation-circle mr-2" />
              {error}
            </div>
          )}
        </div>
      </div>
    )
  }
}
