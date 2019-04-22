export interface ITaskList {
    id: number,
    name: string
}

export interface ITaskShort {
    id: number,
    name: string,
    status: string
}

export interface ITaskLong {
    id: number,
    name: string,
    created_at: string,
    due_on: string,
    status: string
}